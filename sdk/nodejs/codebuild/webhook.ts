// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.
 * 
 * ## Example Usage
 * 
 * ### Bitbucket and GitHub
 * 
 * When working with [Bitbucket](https://bitbucket.org) and [GitHub](https://github.com) source CodeBuild webhooks, the CodeBuild service will automatically create (on `aws.codebuild.Webhook` resource creation) and delete (on `aws.codebuild.Webhook` resource deletion) the Bitbucket/GitHub repository webhook using its granted OAuth permissions. This behavior cannot be controlled by this provider.
 * 
 * > **Note:** The AWS account that this provider uses to create this resource *must* have authorized CodeBuild to access Bitbucket/GitHub's OAuth API in each applicable region. This is a manual step that must be done *before* creating webhooks with this resource. If OAuth is not configured, AWS will return an error similar to `ResourceNotFoundException: Could not find access token for server type github`. More information can be found in the CodeBuild User Guide for [Bitbucket](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-bitbucket-pull-request.html) and [GitHub](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-pull-request.html).
 * 
 * > **Note:** Further managing the automatically created Bitbucket/GitHub webhook with the `bitbucketHook`/`githubRepositoryWebhook` resource is only possible with importing that resource after creation of the `aws.codebuild.Webhook` resource. The CodeBuild API does not ever provide the `secret` attribute for the `aws.codebuild.Webhook` resource in this scenario.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.codebuild.Webhook("example", {
 *     filterGroups: [{
 *         filters: [
 *             {
 *                 pattern: "PUSH",
 *                 type: "EVENT",
 *             },
 *             {
 *                 pattern: "master",
 *                 type: "HEAD_REF",
 *             },
 *         ],
 *     }],
 *     projectName: aws_codebuild_project_example.name,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown.
 */
export class Webhook extends pulumi.CustomResource {
    /**
     * Get an existing Webhook resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebhookState, opts?: pulumi.CustomResourceOptions): Webhook {
        return new Webhook(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:codebuild/webhook:Webhook';

    /**
     * Returns true if the given object is an instance of Webhook.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Webhook {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Webhook.__pulumiType;
    }

    /**
     * A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filterGroup` over `branchFilter`.
     */
    public readonly branchFilter!: pulumi.Output<string | undefined>;
    /**
     * Information about the webhook's trigger. Filter group blocks are documented below.
     */
    public readonly filterGroups!: pulumi.Output<outputs.codebuild.WebhookFilterGroup[] | undefined>;
    /**
     * The CodeBuild endpoint where webhook events are sent.
     */
    public /*out*/ readonly payloadUrl!: pulumi.Output<string>;
    /**
     * The name of the build project.
     */
    public readonly projectName!: pulumi.Output<string>;
    /**
     * The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
     */
    public /*out*/ readonly secret!: pulumi.Output<string>;
    /**
     * The URL to the webhook.
     */
    public /*out*/ readonly url!: pulumi.Output<string>;

    /**
     * Create a Webhook resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WebhookArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WebhookArgs | WebhookState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as WebhookState | undefined;
            inputs["branchFilter"] = state ? state.branchFilter : undefined;
            inputs["filterGroups"] = state ? state.filterGroups : undefined;
            inputs["payloadUrl"] = state ? state.payloadUrl : undefined;
            inputs["projectName"] = state ? state.projectName : undefined;
            inputs["secret"] = state ? state.secret : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as WebhookArgs | undefined;
            if (!args || args.projectName === undefined) {
                throw new Error("Missing required property 'projectName'");
            }
            inputs["branchFilter"] = args ? args.branchFilter : undefined;
            inputs["filterGroups"] = args ? args.filterGroups : undefined;
            inputs["projectName"] = args ? args.projectName : undefined;
            inputs["payloadUrl"] = undefined /*out*/;
            inputs["secret"] = undefined /*out*/;
            inputs["url"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Webhook.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Webhook resources.
 */
export interface WebhookState {
    /**
     * A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filterGroup` over `branchFilter`.
     */
    readonly branchFilter?: pulumi.Input<string>;
    /**
     * Information about the webhook's trigger. Filter group blocks are documented below.
     */
    readonly filterGroups?: pulumi.Input<pulumi.Input<inputs.codebuild.WebhookFilterGroup>[]>;
    /**
     * The CodeBuild endpoint where webhook events are sent.
     */
    readonly payloadUrl?: pulumi.Input<string>;
    /**
     * The name of the build project.
     */
    readonly projectName?: pulumi.Input<string>;
    /**
     * The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
     */
    readonly secret?: pulumi.Input<string>;
    /**
     * The URL to the webhook.
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Webhook resource.
 */
export interface WebhookArgs {
    /**
     * A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filterGroup` over `branchFilter`.
     */
    readonly branchFilter?: pulumi.Input<string>;
    /**
     * Information about the webhook's trigger. Filter group blocks are documented below.
     */
    readonly filterGroups?: pulumi.Input<pulumi.Input<inputs.codebuild.WebhookFilterGroup>[]>;
    /**
     * The name of the build project.
     */
    readonly projectName: pulumi.Input<string>;
}
