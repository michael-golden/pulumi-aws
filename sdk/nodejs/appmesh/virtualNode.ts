// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an AWS App Mesh virtual node resource.
 * 
 * ## Breaking Changes
 * 
 * Because of backward incompatible API changes (read [here](https://github.com/awslabs/aws-app-mesh-examples/issues/92)), `aws.appmesh.VirtualNode` resource definitions created with provider versions earlier than v2.3.0 will need to be modified:
 * 
 * * Rename the `serviceName` attribute of the `dns` object to `hostname`.
 * 
 * * Replace the `backends` attribute of the `spec` object with one or more `backend` configuration blocks,
 * setting `virtualServiceName` to the name of the service.
 * 
 * The state associated with existing resources will automatically be migrated.
 * 
 * ## Example Usage
 * 
 * ### Basic
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
 *     meshName: aws_appmesh_mesh_simple.id,
 *     spec: {
 *         backends: [{
 *             virtualService: {
 *                 virtualServiceName: "servicea.simpleapp.local",
 *             },
 *         }],
 *         listener: {
 *             portMapping: {
 *                 port: 8080,
 *                 protocol: "http",
 *             },
 *         },
 *         serviceDiscovery: {
 *             dns: {
 *                 hostname: "serviceb.simpleapp.local",
 *             },
 *         },
 *     },
 * });
 * ```
 * 
 * ### AWS Cloud Map Service Discovery
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.servicediscovery.HttpNamespace("example", {});
 * const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
 *     meshName: aws_appmesh_mesh_simple.id,
 *     spec: {
 *         backends: [{
 *             virtualService: {
 *                 virtualServiceName: "servicea.simpleapp.local",
 *             },
 *         }],
 *         listener: {
 *             portMapping: {
 *                 port: 8080,
 *                 protocol: "http",
 *             },
 *         },
 *         serviceDiscovery: {
 *             awsCloudMap: {
 *                 attributes: {
 *                     stack: "blue",
 *                 },
 *                 namespaceName: example.name,
 *                 serviceName: "serviceb1",
 *             },
 *         },
 *     },
 * });
 * ```
 * 
 * ### Listener Health Check
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
 *     meshName: aws_appmesh_mesh_simple.id,
 *     spec: {
 *         backends: [{
 *             virtualService: {
 *                 virtualServiceName: "servicea.simpleapp.local",
 *             },
 *         }],
 *         listener: {
 *             healthCheck: {
 *                 healthyThreshold: 2,
 *                 intervalMillis: 5000,
 *                 path: "/ping",
 *                 protocol: "http",
 *                 timeoutMillis: 2000,
 *                 unhealthyThreshold: 2,
 *             },
 *             portMapping: {
 *                 port: 8080,
 *                 protocol: "http",
 *             },
 *         },
 *         serviceDiscovery: {
 *             dns: {
 *                 hostname: "serviceb.simpleapp.local",
 *             },
 *         },
 *     },
 * });
 * ```
 * 
 * ### Logging
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
 *     meshName: aws_appmesh_mesh_simple.id,
 *     spec: {
 *         backends: [{
 *             virtualService: {
 *                 virtualServiceName: "servicea.simpleapp.local",
 *             },
 *         }],
 *         listener: {
 *             portMapping: {
 *                 port: 8080,
 *                 protocol: "http",
 *             },
 *         },
 *         logging: {
 *             accessLog: {
 *                 file: {
 *                     path: "/dev/stdout",
 *                 },
 *             },
 *         },
 *         serviceDiscovery: {
 *             dns: {
 *                 hostname: "serviceb.simpleapp.local",
 *             },
 *         },
 *     },
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_node.html.markdown.
 */
export class VirtualNode extends pulumi.CustomResource {
    /**
     * Get an existing VirtualNode resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNodeState, opts?: pulumi.CustomResourceOptions): VirtualNode {
        return new VirtualNode(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:appmesh/virtualNode:VirtualNode';

    /**
     * Returns true if the given object is an instance of VirtualNode.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VirtualNode {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VirtualNode.__pulumiType;
    }

    /**
     * The ARN of the virtual node.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The creation date of the virtual node.
     */
    public /*out*/ readonly createdDate!: pulumi.Output<string>;
    /**
     * The last update date of the virtual node.
     */
    public /*out*/ readonly lastUpdatedDate!: pulumi.Output<string>;
    /**
     * The name of the service mesh in which to create the virtual node.
     */
    public readonly meshName!: pulumi.Output<string>;
    /**
     * The name to use for the virtual node.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The virtual node specification to apply.
     */
    public readonly spec!: pulumi.Output<outputs.appmesh.VirtualNodeSpec>;
    /**
     * A map of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a VirtualNode resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VirtualNodeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VirtualNodeArgs | VirtualNodeState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VirtualNodeState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["createdDate"] = state ? state.createdDate : undefined;
            inputs["lastUpdatedDate"] = state ? state.lastUpdatedDate : undefined;
            inputs["meshName"] = state ? state.meshName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["spec"] = state ? state.spec : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as VirtualNodeArgs | undefined;
            if (!args || args.meshName === undefined) {
                throw new Error("Missing required property 'meshName'");
            }
            if (!args || args.spec === undefined) {
                throw new Error("Missing required property 'spec'");
            }
            inputs["meshName"] = args ? args.meshName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["spec"] = args ? args.spec : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["createdDate"] = undefined /*out*/;
            inputs["lastUpdatedDate"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(VirtualNode.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VirtualNode resources.
 */
export interface VirtualNodeState {
    /**
     * The ARN of the virtual node.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The creation date of the virtual node.
     */
    readonly createdDate?: pulumi.Input<string>;
    /**
     * The last update date of the virtual node.
     */
    readonly lastUpdatedDate?: pulumi.Input<string>;
    /**
     * The name of the service mesh in which to create the virtual node.
     */
    readonly meshName?: pulumi.Input<string>;
    /**
     * The name to use for the virtual node.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The virtual node specification to apply.
     */
    readonly spec?: pulumi.Input<inputs.appmesh.VirtualNodeSpec>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a VirtualNode resource.
 */
export interface VirtualNodeArgs {
    /**
     * The name of the service mesh in which to create the virtual node.
     */
    readonly meshName: pulumi.Input<string>;
    /**
     * The name to use for the virtual node.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The virtual node specification to apply.
     */
    readonly spec: pulumi.Input<inputs.appmesh.VirtualNodeSpec>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
