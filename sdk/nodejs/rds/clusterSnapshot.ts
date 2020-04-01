// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the [`aws.rds.Snapshot` resource](https://www.terraform.io/docs/providers/aws/r/db_snapshot.html).
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.rds.ClusterSnapshot("example", {
 *     dbClusterIdentifier: aws_rds_cluster_example.id,
 *     dbClusterSnapshotIdentifier: "resourcetestsnapshot1234",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_cluster_snapshot.html.markdown.
 */
export class ClusterSnapshot extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSnapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterSnapshotState, opts?: pulumi.CustomResourceOptions): ClusterSnapshot {
        return new ClusterSnapshot(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:rds/clusterSnapshot:ClusterSnapshot';

    /**
     * Returns true if the given object is an instance of ClusterSnapshot.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSnapshot {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSnapshot.__pulumiType;
    }

    /**
     * Specifies the allocated storage size in gigabytes (GB).
     */
    public /*out*/ readonly allocatedStorage!: pulumi.Output<number>;
    /**
     * List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
     */
    public /*out*/ readonly availabilityZones!: pulumi.Output<string[]>;
    /**
     * The DB Cluster Identifier from which to take the snapshot.
     */
    public readonly dbClusterIdentifier!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
     */
    public /*out*/ readonly dbClusterSnapshotArn!: pulumi.Output<string>;
    /**
     * The Identifier for the snapshot.
     */
    public readonly dbClusterSnapshotIdentifier!: pulumi.Output<string>;
    /**
     * Specifies the name of the database engine.
     */
    public /*out*/ readonly engine!: pulumi.Output<string>;
    /**
     * Version of the database engine for this DB cluster snapshot.
     */
    public /*out*/ readonly engineVersion!: pulumi.Output<string>;
    /**
     * If storageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
     */
    public /*out*/ readonly kmsKeyId!: pulumi.Output<string>;
    /**
     * License model information for the restored DB cluster.
     */
    public /*out*/ readonly licenseModel!: pulumi.Output<string>;
    /**
     * Port that the DB cluster was listening on at the time of the snapshot.
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    public /*out*/ readonly snapshotType!: pulumi.Output<string>;
    public /*out*/ readonly sourceDbClusterSnapshotArn!: pulumi.Output<string>;
    /**
     * The status of this DB Cluster Snapshot.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Specifies whether the DB cluster snapshot is encrypted.
     */
    public /*out*/ readonly storageEncrypted!: pulumi.Output<boolean>;
    /**
     * A mapping of tags to assign to the DB cluster.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The VPC ID associated with the DB cluster snapshot.
     */
    public /*out*/ readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a ClusterSnapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterSnapshotArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterSnapshotArgs | ClusterSnapshotState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ClusterSnapshotState | undefined;
            inputs["allocatedStorage"] = state ? state.allocatedStorage : undefined;
            inputs["availabilityZones"] = state ? state.availabilityZones : undefined;
            inputs["dbClusterIdentifier"] = state ? state.dbClusterIdentifier : undefined;
            inputs["dbClusterSnapshotArn"] = state ? state.dbClusterSnapshotArn : undefined;
            inputs["dbClusterSnapshotIdentifier"] = state ? state.dbClusterSnapshotIdentifier : undefined;
            inputs["engine"] = state ? state.engine : undefined;
            inputs["engineVersion"] = state ? state.engineVersion : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["licenseModel"] = state ? state.licenseModel : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["snapshotType"] = state ? state.snapshotType : undefined;
            inputs["sourceDbClusterSnapshotArn"] = state ? state.sourceDbClusterSnapshotArn : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["storageEncrypted"] = state ? state.storageEncrypted : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as ClusterSnapshotArgs | undefined;
            if (!args || args.dbClusterIdentifier === undefined) {
                throw new Error("Missing required property 'dbClusterIdentifier'");
            }
            if (!args || args.dbClusterSnapshotIdentifier === undefined) {
                throw new Error("Missing required property 'dbClusterSnapshotIdentifier'");
            }
            inputs["dbClusterIdentifier"] = args ? args.dbClusterIdentifier : undefined;
            inputs["dbClusterSnapshotIdentifier"] = args ? args.dbClusterSnapshotIdentifier : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["allocatedStorage"] = undefined /*out*/;
            inputs["availabilityZones"] = undefined /*out*/;
            inputs["dbClusterSnapshotArn"] = undefined /*out*/;
            inputs["engine"] = undefined /*out*/;
            inputs["engineVersion"] = undefined /*out*/;
            inputs["kmsKeyId"] = undefined /*out*/;
            inputs["licenseModel"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
            inputs["snapshotType"] = undefined /*out*/;
            inputs["sourceDbClusterSnapshotArn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["storageEncrypted"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ClusterSnapshot.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ClusterSnapshot resources.
 */
export interface ClusterSnapshotState {
    /**
     * Specifies the allocated storage size in gigabytes (GB).
     */
    readonly allocatedStorage?: pulumi.Input<number>;
    /**
     * List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
     */
    readonly availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The DB Cluster Identifier from which to take the snapshot.
     */
    readonly dbClusterIdentifier?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
     */
    readonly dbClusterSnapshotArn?: pulumi.Input<string>;
    /**
     * The Identifier for the snapshot.
     */
    readonly dbClusterSnapshotIdentifier?: pulumi.Input<string>;
    /**
     * Specifies the name of the database engine.
     */
    readonly engine?: pulumi.Input<string>;
    /**
     * Version of the database engine for this DB cluster snapshot.
     */
    readonly engineVersion?: pulumi.Input<string>;
    /**
     * If storageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * License model information for the restored DB cluster.
     */
    readonly licenseModel?: pulumi.Input<string>;
    /**
     * Port that the DB cluster was listening on at the time of the snapshot.
     */
    readonly port?: pulumi.Input<number>;
    readonly snapshotType?: pulumi.Input<string>;
    readonly sourceDbClusterSnapshotArn?: pulumi.Input<string>;
    /**
     * The status of this DB Cluster Snapshot.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * Specifies whether the DB cluster snapshot is encrypted.
     */
    readonly storageEncrypted?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the DB cluster.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The VPC ID associated with the DB cluster snapshot.
     */
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterSnapshot resource.
 */
export interface ClusterSnapshotArgs {
    /**
     * The DB Cluster Identifier from which to take the snapshot.
     */
    readonly dbClusterIdentifier: pulumi.Input<string>;
    /**
     * The Identifier for the snapshot.
     */
    readonly dbClusterSnapshotIdentifier: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the DB cluster.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
